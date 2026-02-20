<!DOCTYPE html>
<html>
<head>
  <title>Upload Image</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      height: 100vh;
      background: url("{{ url_for('static', filename='bg.jpg') }}") no-repeat center center fixed;
      background-size: cover;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: Arial, sans-serif;
    }

    .container {
      background-color: rgba(0, 0, 0, 0.7);
      padding: 40px 60px;
      border-radius: 12px;
      text-align: center;
      color: white;
    }

    input[type="file"],
    input[type="submit"] {
      margin: 15px 0;
      padding: 10px;
      font-size: 16px;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Upload a Fruit or Vegetable Image</h2>
    <form method="POST" action="/predict" enctype="multipart/form-data">
      <input type="file" name="image" required><br>
      <input type="submit" value="Predict">
    </form>
  </div>
</body>
</html>
