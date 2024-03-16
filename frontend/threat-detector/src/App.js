import React, { useState, useEffect } from 'react';
import { CircularProgress, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      {data ? (
        <div>
          <h1>Table Data</h1>
          {data.map((table, index) => (
            <div key={index} style={{ marginBottom: '20px' }}>
              <h2>Table {table.table}</h2>
              <TableContainer component={Paper}>
                <Table>
                  <TableHead>
                    <TableRow>
                      {Object.keys(table.values).map((key, index) => (
                        <TableCell key={index}>{key}</TableCell>
                      ))}
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    <TableRow>
                      {Object.values(table.values).map((value, index) => (
                        <TableCell key={index}>{value}</TableCell>
                      ))}
                    </TableRow>
                  </TableBody>
                </Table>
              </TableContainer>
            </div>
          ))}
        </div>
      ) : (
        <div style={{ textAlign: 'center' }}>
          <CircularProgress />
        </div>
      )}
    </div>
  );
}

export default App;
