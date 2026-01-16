fetch("http://localhost:5000/roi")
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText =
      "ROI: " + data.roi + "%";
  });
