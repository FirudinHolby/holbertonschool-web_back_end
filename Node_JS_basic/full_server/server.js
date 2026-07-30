import express from 'express';
import router from './routes/index';

const app = express();

// Yaratdığımız route strukturunu istifadə edirik
app.use('/', router);

app.listen(1245);

export default app;
