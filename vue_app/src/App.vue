<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">

  </div>
</template>


<script>
const SECRET_NUM = 'IamTajalIslam'
    var jwt = require('jsonwebtoken');
    var token = jwt.sign({username: 'Tajal', password: "islam"}, SECRET_NUM);
    // eslint-disable-next-line no-console
    console.log(token)

export default {
  name: 'app',
  components: {

  },
  data(){
    return{

    }
  },
  created() {
            fetch("http://127.0.0.1:8000/api/comunication/", {
                method: 'GET',
                headers: {
                    Authorization:token,
                    'Content-Type': 'application/json',
                    // 'Access-Control-Allow-Origin': true
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },

            })
                .then((response) => {
                    return response
                }).then((data) => {
                // eslint-disable-next-line no-console
                console.log(data)
            })
        }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
