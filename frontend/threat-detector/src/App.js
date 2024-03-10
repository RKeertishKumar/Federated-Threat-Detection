import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      {data ? (
        <div>
          <p>Message: {data}</p>
        </div>
      ) : (
        <p>Loading... {data}</p>
      )}
    </div>
  );
}

export default App;
