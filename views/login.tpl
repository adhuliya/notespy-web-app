<!DOCTYPE html>
<%
setdefault('failed', False)
%>
<html>
<body>
%if failed:
<b>Bad user id or password</b>
%end
<form method="post" action="login">
<input type="text" name="uid" autofocus/>
<input type="password" name="pwd"/>
<input type="submit" value="submit"/>
</form>
</body>
</html>
