import csv
def error_detector(source,target):
    with open('report.html','w') as file:
        output =    '''<html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    html{
                    overflow:hidden;
                    }
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
                      width:100%;
                      
      
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
                      </tr>'''
        

        for i in range(len(source)):
            
            source_val=source[i]
            target_val=target[i]
            
            
            source_val_err,target_val_err,src_err,trg_err='','','',''


                
            length =min(len(source_val),len(target_val))
            source_val_add = '''<span class='error'>%s</span>'''%(source_val[length:])
            target_val_add = '''<span class='error'>%s</span>'''%(target_val[length:])
            source_val = source_val[:length]
            target_val = target_val[:length]
        

            
            
            for j in range(len(source_val)):
                
                if source_val[j]!=target_val[j]:
                    src_err+=source_val[j]
                    trg_err+=target_val[j]
                    
                else:
                    if (src_err or trg_err):
                        source_val_err+='''<span class='error'>%s</span>'''%(src_err)
                        target_val_err+='''<span class='error'>%s</span>'''%(trg_err)
                        src_err,trg_err='',''
                    
                    source_val_err+=source_val[j]
                    target_val_err+=target_val[j]
            if (src_err or trg_err):
                source_val_err+='''<span class='error'>%s</span>'''%(src_err)
                target_val_err+='''<span class='error'>%s</span>'''%(trg_err)
            
            source_val_err+=source_val_add
            target_val_err+=target_val_add
            output+='''
              <tr>
                <td>%s</td>
                <td>%s</td>
              </tr>
            '''%(source_val_err,target_val_err)
        
        

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
with open('test.csv','r') as file1:
    a=list(csv.DictReader(file1))
    source,target=[],[]
    for i in range(len(a)):
        source.append(a[i]['Source'])
        target.append(a[i]['Target'])
    error_detector(source,target)
