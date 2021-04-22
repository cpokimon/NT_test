# NT_test

#### Quick start:
 
  1. git clone https://github.com/cpokimon/NT_test.git
  2. open terminal
  3. docker build .  ----> then copy part of id (f.e you see sha256:c477cf1de101853b, you have copy just c477cf1 )
  4. docker run -p 5000:5000 <container_id>
  
##### Now you can send GET requests with raw JSON to the localhost:5000/api/resolve and receive results.
