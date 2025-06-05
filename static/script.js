document.getElementById("upload-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("image-upload");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select an image.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      alert("Error: " + data.error);
    } else {
      document.getElementById("prediction").innerText = "Prediction: " + data.prediction;
      document.getElementById("confidence").innerText = "Confidence: " + data.confidence + "%";
    }

  } catch (error) {
    console.error("Error:", error);
    alert("Failed to fetch prediction.");
  }
});
