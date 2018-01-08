<html>
	<head>
		<title>My Shop</title>
	</head>
	<body>
		<h1>Welcome to my shop</h1>
		<u1>
			<?php
				$servername = "mysql";
				$username = "root";
				$password = "root";
				$database = "test_db";
				$conn = new mysqli($servername, $username, $password, $database);

				
				if ($conn->connect_error) {
				    die("Connection failed: " . $conn->connect_error);
				}
				
				//Executing sql statements

				$db_query = $_GET['month'];
				$q_stmt = $conn->prepare('SELECT * FROM months WHERE id = ?');
				$q_stmt->bind_param('i',$db_query);
				$q_stmt->execute();
				$result = $q_stmt->get_result();
				while ($row = $result->fetch_assoc()) {
				    echo "<br>";
				    echo " Month id = " . $row['month_id'] . ", Month name = " . $row['month_name'];
				}
				mysqli_close($conn);

			?>
		</u1>
	</body>
</html>