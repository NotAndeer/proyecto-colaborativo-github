document.getElementById("scan-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const baseIp = document.getElementById("base-ip").value;
  const tbody = document.querySelector("#results tbody");
  tbody.innerHTML = "<tr><td colspan='2'>Escaneando...</td></tr>";

  try {
    const res = await fetch(`http://localhost:5000/scan?base_ip=${baseIp}`);
    const data = await res.json();
    tbody.innerHTML = "";

    if (data.length === 0) {
      tbody.innerHTML = "<tr><td colspan='2'>No se encontraron dispositivos.</td></tr>";
      return;
    }

    data.forEach(host => {
      const row = `<tr><td>${host.ip}</td><td>${host.status}</td></tr>`;
      tbody.innerHTML += row;
    });
  } catch (error) {
    tbody.innerHTML = "<tr><td colspan='2'>Error al conectar con el backend.</td></tr>";
  }
});
