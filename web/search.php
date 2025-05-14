<html>
    <head><title>Search tools</title></head>
<body>
<?php if (!empty($_POST)): ?>
    $urls = htmlspecialchars($_POST["urls"]);

    if (substr_count(',') > 1) {
        $filename = "links.php";
        $fh = fopen($filename, "w");
        fwrite($fh, $urls);
        fclose($fh);

        $command = "python3 accessibility.py -f ${filename}";
    } else {
        $command = "python3 accessibility.py -u ${urls}";
    }

    $escaped_command = escapeshellcmd($command);
    
    system($escaped_command);

    //remove the current json files

<?php else: ?>
    <h3>Accessibility</h3>
    <p>Please enter a comma separated list of URLs to run accessibility</p>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        List: <input type="textarea" name="urls"><br>
        <input type="submit">
    </form>
<?php endif; ?>
</body>
</html>