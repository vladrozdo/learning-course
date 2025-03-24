import React, { useEffect, useState } from "react";

function App() {
  const [speedData, setSpeedData] = useState(null);

  useEffect(() => {
    fetch("/api/speedtest")
      .then((response) => response.json())
      .then((data) => setSpeedData(data));
  }, []);

  return (
    <div>
      <h1>Speedtest Results</h1>
      {speedData ? (
        <div>
          <p>Download Speed: {speedData.download} Mbps</p>
          <p>Upload Speed: {speedData.upload} Mbps</p>
          <p>Ping: {speedData.ping} ms</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
