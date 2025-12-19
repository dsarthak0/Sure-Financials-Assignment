import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Select a PDF");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult(null);

    const res = await fetch("http://127.0.0.1:8000/parse", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h2>💳 Credit Card Statement Parser</h2>

      <input type="file" accept=".pdf" onChange={e => setFile(e.target.files[0])} />
      <br /><br />

      <button onClick={handleUpload}>Upload & Parse</button>

      {loading && <p>Parsing...</p>}
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}

export default App;
