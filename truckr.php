<?php
    $conn = mysqli_connect('localhost', 'root', 'brew', 'truckr');
    $sql = "select * from coordinates where id=(select max(id) from coordinates)";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);

    echo json_encode($row);
?>

