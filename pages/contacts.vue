<template lang="html">
  <section>
    <div class="container">
      <h2>Онлайн-музей реликвий оставшихся с Великой Отечественной войны</h2>
      <div class="chatbot" v-if="see">
        <div class="phone" id="om">
          <p class="messagebot">Здравствуйте! Я, бот помощник сайта музей победы</p>
          <p class="messagebot">Здесь, вы можете добавить статью о вашей семейной реликвии</p>
          <p class="messagebot"> Для добавления, пропишите команду /add.</p>
          <p class="messagebot"> Для добавления, пропишите команду /add.</p>
          <p class="messagebot">Для помощи, пропишпте команду /help.</p>
          <input type="text" class="or" id="kl">
        </div>
      </div>
      <div class="main">
        <div class="row row-cols-1 row-cols-md-3 g-4">
          <div v-for="item in more" :key="item.id">
            <div class="col">
              <div class="card" @click.prevent="openUser(item)">
                <img :src="require(`../assets/rel/${item.id+1}.jpg`)" class="card-img-top" alt="...">
                <div class="card-body">
                  <h5 style="color:white" class="card-title">{{item.zag}}</h5>
                  <p class="card-text">{{item.text}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default{
  data(){
    return{
      see: false,
      more: [
        {
          id: 0,
          zag: "Первая реликвия",
          text:"А также реплицированные с зарубежных источников, современные исследования, инициированные исключительно синтетически, объявлены нарушающими общечеловеческие нормы этики и морали.",
        },
        {
          id: 1,
          zag: "Вторая реликвия",
          text:"А также реплицированные с зарубежных источников, современные исследования, инициированные исключительно синтетически, объявлены нарушающими общечеловеческие нормы этики и морали.",
        },
        {
          id: 2,
          zag: "Третья реликвия",
          text:"А также реплицированные с зарубежных источников, современные исследования, инициированные исключительно синтетически, объявлены нарушающими общечеловеческие нормы этики и морали.",
        },
        {
          id: 3,
          zag: "Четвертая реликвия",
          text:"А также реплицированные с зарубежных источников, современные исследования, инициированные исключительно синтетически, объявлены нарушающими общечеловеческие нормы этики и морали.",
        },
      ]
    }
  },
  mounted(){
    let dic = document.getElementById('om')
    let self = this
    const requestURL = '?offset=0&limit=10' /*до вопроса здесь твоя ссылка,после вопроса параметры которые надо получить*/

    function sendRequest(method, url, body = null) {
        return new Promise((resolve, reject) => {
          const xhr = new XMLHttpRequest()

          xhr.open(method, url)

          xhr.responseType = 'json'
          xhr.setRequestHeader('Content-Type', 'application/json')


          xhr.onload = () => {
            let stas = xhr.response
          }

          xhr.onerror = () => {
            reject(xhr.response)
          }

          xhr.send(JSON.stringify(body))
        })
      }



      sendRequest('GET', requestURL)
        .then(data => console.log(data))
        .catch(err => console.log(err))


      document.onkeydown = function(e){
      switch (e.keyCode) {
          case 90:
              self.see = true
              console.log('stas');
              console.log(self.see);
              break;
          case 88:
              self.see = false
              break;
          case 13:
              let kl = document.getElementById('kl').value
              let av = document.createElement("div");
              av.innerHTML = av
              av.classList.add('ok')
              let dic = document.getElementById('om')
              break;
          default:
              console.log(e.keyCode);
      }
  };

 },
 methods:{
   openUser(item) {
      this.$router.push('/event/' + item.id)

    },
 }
}
</script>

<style lang="css" scoped>
.card{
  background-color: #333333;
  min-width: 300px;
}
.messagebot{
  background-color: #9999FF;
  padding: 5px;
  max-width: 200px;
  margin-left: -250px;
}
.message{
  background-color: #0000CC;
  padding: 5px;
  max-width: 200px;
  margin-left: 250px;
}
.or{
  border-radius: 2px;
  background-color: #222222;
  border: none;
  color: white;
}
.phone{
  width: 500px;
  background-color: white;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  padding: 10px;
}
input{
  width: 70%;
}
button{
  margin-left: 5px;
}
.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
  margin-bottom: 100px;
}
.main{
  width: 80%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  margin-top: 20px;
}
h2{
  color: white;
}
.in{
  width: 80%;
  display: flex;
  justify-content: center;
}
p{
  color: white;
  margin:10px;
}
@media (max-width: 450px){
  .main{
    width: 100%;
  }
}
</style>
