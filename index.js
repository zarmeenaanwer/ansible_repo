const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, this is a simple Node.js web application!');
});

const port = 3000;
const server = app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running on port ${port}`);
});
