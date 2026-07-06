const MAX_NAME = 120;
const MAX_EMAIL = 200;
const MAX_MESSAGE = 5000;

export async function onRequestPost(context) {
  const { request, env } = context;

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  if (body.website) {
    return json({ ok: true });
  }

  const name = clean(body.name, MAX_NAME);
  const email = clean(body.email, MAX_EMAIL);
  const message = clean(body.message, MAX_MESSAGE);

  if (!name || !email || !message) {
    return json({ error: "missing_fields" }, 400);
  }
  if (!isEmail(email)) {
    return json({ error: "invalid_email" }, 400);
  }

  const to = env.CONTACT_TO || "consultas@alexkore.com";
  const from = env.CONTACT_FROM || "consultas@alexkore.com";
  const subject = `Korelabs — ${name}`;
  const text = `Nombre: ${name}\nEmail: ${email}\n\n${message}`;

  try {
    if (env.EMAIL) {
      await sendViaCloudflare(env.EMAIL, { from, to, replyTo: email, subject, text });
    } else if (env.RESEND_API_KEY) {
      await sendViaResend(env.RESEND_API_KEY, { from, to, replyTo: email, subject, text });
    } else if (env.WEB3FORMS_ACCESS_KEY) {
      await sendViaWeb3Forms(env.WEB3FORMS_ACCESS_KEY, { name, email, message, subject });
    } else {
      return json({ error: "not_configured" }, 503);
    }
    return json({ ok: true });
  } catch {
    return json({ error: "send_failed" }, 500);
  }
}

async function sendViaCloudflare(emailBinding, { from, to, replyTo, subject, text }) {
  const { EmailMessage } = await import("cloudflare:email");
  const raw = [
    `From: Korelabs <${from}>`,
    `To: ${to}`,
    `Reply-To: ${replyTo}`,
    `Subject: ${subject}`,
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=UTF-8",
    "",
    text,
  ].join("\r\n");
  const msg = new EmailMessage(from, to, raw);
  await emailBinding.send(msg);
}

async function sendViaResend(apiKey, { from, to, replyTo, subject, text }) {
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: `Korelabs <${from}>`,
      to: [to],
      reply_to: replyTo,
      subject,
      text,
    }),
  });
  if (!res.ok) throw new Error("resend_failed");
}

async function sendViaWeb3Forms(accessKey, { name, email, message, subject }) {
  const res = await fetch("https://api.web3forms.com/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({
      access_key: accessKey,
      name,
      email,
      message,
      subject,
      from_name: "Korelabs Web",
    }),
  });
  const data = await res.json();
  if (!res.ok || !data.success) throw new Error("web3forms_failed");
}

function clean(value, max) {
  if (typeof value !== "string") return "";
  return value.trim().slice(0, max);
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}
