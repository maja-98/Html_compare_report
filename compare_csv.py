import csv
def error_detector(source,target):
    with open('report.html','w') as file:
        output =    '''<html>
            <head>
                <style>
                    h1{
                    text-align:center;
                    font-family: "Lucida Console", "Courier New", monospace;
                    background-color: #00cccc;
                    color: #e6ffff;
                    border-radius:2px;
    
                    }
                    th,td {
                        border: 2px solid black;
                        background-color: #e6ffff;
                        
                        }
                    td{
                    padding:10px;
                    }
                    .error{
                    background-color : yellow;
                    }
                    html{
                    background-color:#00ffff;
                    }
                    div{

                      display:flex;
    
                      justify-content:center;
                      height:500px;
                      overflow-x:hidden;
                      overflow-y:scroll;
                      width:50%;
                      
      
                    }

                    .align-center{
                      display:flex;
                      flex-direction:column;
                      align-items:center;
                    }
                    p{
                    margin:5px;
                </style>
                <title> Text Compare </title> 
            </head>
            <body class='align-center'>
                <h1>Error Report </h1>
                <div>
                    <table >
                      <tr>
                        <th>Source</th>
                        <th>Target</th>
                        <th>Error</th>
                      </tr>'''
        

        for i in range(len(source)):
            
            source_val=source[i]
            target_val=target[i]
            
            val=''
            error=''

            if len(source_val)>len(target_val):
                main=source_val
            else:
                main= target_val
                
            length =max(len(source_val),len(target_val))
            source_val = source_val.ljust(length,' ')
            target_val = target_val.ljust(length,' ')
            
            for j in range(len(source_val)):
                
                if source_val[j]!=target_val[j]:
                    error+=main[j]
                    
                else:
                    if error:
                        val+='''<span class='error'>%s</span>'''%(error)
                        error=''
                    
                    val+=main[j]
            if error:
                val+='''<span class='error'>%s</span>'''%(error)
            

            output+='''
              <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
              </tr>
            '''%(source_val,target_val,val)
        
        

        output+='''
                            </table>
                            
                        </div>
                        <footer class='align-center'>
                            <p>This comparing source and target by letterwise!!!</p>
                            <p>Will update more soon!!!</p>
                            <small>&#169; MAJA</small>
                        </footer> 
                    </body>
                </html>'''
        #print(output)
        file.write(output)
        print("Done")
with open('test.csv','r') as ajmal:
    a=list(csv.DictReader(ajmal))
    source,target=[],[]
    for i in range(len(a)):
        source.append(a[i]['Source'])
        target.append(a[i]['Target'])
    error_detector(source,target)
