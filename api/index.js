const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/api/fortune', (req, res) => {
  res.json({ message: 'Your fortune here' });
});

app.listen(port, () => {
  console.log(`API running on port ${port}`);
});
