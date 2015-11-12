<form action="/diary" method="post">
      输入：<input name="content" type="text" />
            <input value="确认" type="submit" />


          % if type(content) is list: 
      		%   for line in content: 
                <br/> {{line}} <br/>
          %   end
          % else: 
            <br/> {{content}} <br/>
