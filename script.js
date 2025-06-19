// Sample WebDriver script for JMeter
driver.get("https://www.your-elearning-platform.com");
driver.findElement(By.name("username")).sendKeys("testuser");
driver.findElement(By.name("password")).sendKeys("testpassword");
driver.findElement(By.name("password")).sendKeys(Keys.RETURN);