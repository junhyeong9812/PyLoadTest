document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("testForm");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const payload = {
      url: formData.get("url"),
      method: formData.get("method"),
      params: JSON.parse(formData.get("params") || "{}"),
      headers: JSON.parse(formData.get("headers") || "{}"),
      body: formData.get("body"),
      cookies: JSON.parse(formData.get("cookies") || "{}"),
      total_requests: parseInt(formData.get("total_requests")),
      threads: parseInt(formData.get("threads")),
    };

    const res = await fetch("/load-test", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const result = await res.json();
    document.getElementById("result").textContent = JSON.stringify(
      result,
      null,
      2
    );
  });
});
