<?php
/*
筛选机制
评分机制
上传文件
输出文件
保存上传数据库
*/?>
<html>
<head>
<meta charset="utf-8">
<title>admin</title>
</head>
<body>

<form action="upload_file.php" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <input type="file" name="file" id="file"><br>
    <input type="submit" name="submit" value="提交">
</form>

</body>
</html>