

<html>
	    <body>
          	<h1> Cen的日记  </h1>
        	<form action="/diary" method="post">
            输入: <input name="content" type="text" />
            <input value="确认" type="submit" />
        	</form>

        	<p> 输入内容 ：</p>
        	  <tr>
        		% if content:
        		<td>{{content}}</td>
        		% end
        	  </tr>

        </body>
</html>
