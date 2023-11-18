const express = require('express');
const { MongoClient } = require('mongodb');
const cors = require('cors');
const { ObjectId } = require('mongodb');



const app = express();
const port = 3001;
const mongoURI = 'mongodb://localhost:27017';
const dbName = 'User';
const collectionName = 'Ambulance';
const collectionName2 = 'Appointment';
const collectionName3 = 'admin';

app.use(cors());
app.use(express.json());

// Handle unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Handle the error, e.g., log it or exit the process
});

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
  // Handle the error, e.g., log it or exit the process
});

app.post('/api/ambulance/request', async (req, res) => {
  let client;

  try {
    const { latitude, longitude, mobileNumber } = req.body;

    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const ambulanceRequest = {
      location: { type: 'Point', coordinates: [longitude, latitude] },
      mobileNumber,
    };

    await collection.insertOne(ambulanceRequest);

    res.json({ message: 'Ambulance request received successfully' });
  } catch (error) {
    console.error('Error handling ambulance request:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.post('/api/appointment', async (req, res) => {
  let client;

  try {
    const formData = req.body;

    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName2);

    await collection.insertOne(formData);

    res.json({ message: 'Appointment scheduled successfully' });
  } catch (error) {
    console.error('Error scheduling appointment:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.post('/api/login', async (req, res) => {
  let client;

  try {
    const { username, password } = req.body;

    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName3);

    const user = await collection.findOne({ username, password });

    if (user) {
      res.json({ message: 'Login successful' });
    } else {
      res.status(401).json({ error: 'Invalid credentials' });
    }
  } catch (error) {
    console.error('Error during login:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.get('/api/ambulance-requests', async (req, res) => {
  let client;

  try {
    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const ambulanceRequests = await collection.find().toArray();

    res.json(ambulanceRequests);
  } catch (error) {
    console.error('Error fetching ambulance requests:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.get('/api/appointment-request', async (req, res) => {
  let client;

  try {
    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName2);

    const ambulanceRequests = await collection.find().toArray();

    res.json(ambulanceRequests);
  } catch (error) {
    console.error('Error fetching ambulance requests:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.delete('/api/appointment-request/:id', async (req, res) => {
  let client;
  try {
    const { id } = req.params;

    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName2);

    // Convert the string ID to ObjectId
    const objectId = new ObjectId(id);

    // Delete the appointment with the specified ID
    const result = await collection.deleteOne({ _id: objectId });

    if (result.deletedCount === 1) {
      res.json({ message: 'Appointment deleted successfully' });
    } else {
      res.status(404).json({ error: 'Appointment not found' });
    }
  } catch (error) {
    console.error('Error deleting appointment:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.delete('/api/ambulance-request/:id', async (req, res) => {
  let client;
  try {
    const { id } = req.params;

    client = await MongoClient.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    // Convert the string ID to ObjectId
    const objectId = new ObjectId(id);

    // Delete the appointment with the specified ID
    const result = await collection.deleteOne({ _id: objectId });

    if (result.deletedCount === 1) {
      res.json({ message: 'Ambulance deleted successfully' });
    } else {
      res.status(404).json({ error: 'Ambulance request not found' });
    }
  } catch (error) {
    console.error('Error deleting appointment:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  } finally {
    if (client) {
      await client.close();
    }
  }
});


app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
