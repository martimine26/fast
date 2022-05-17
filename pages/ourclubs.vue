<template lang="html">
  <section>
    <div class="container">
      <h1>Наши клубы</h1>
      <div v-for="item in array" :key="item.id" class="main">
        <div class="block">
          <div class="photo" :style="{'background-image': 'url(' + require('@/assets/' + item.logo) + ')'}"></div>
          <div class="text">
            <h4>{{item.text}}</h4>
            <p>{{item.name}}</p>
            <p>{{item.address1}}</p>
            <p>{{item.address2}}</p>
            <p>{{item.address3}}</p>
            <p>{{item.contacts}}</p>
            <a :href="`${item.link}`">Мы во вконтакте</a>
            <h3>Тренеры:</h3>
            <div class="photo1" :style="{'background-image': 'url(' + require('@/assets/' + item.photo1) + ')'}"></div>
            <p>{{item.trener1}}</p>
            <div class="photo1" :style="{'background-image': 'url(' + require('@/assets/' + item.photo2) + ')'}" :id="item.id + 'ok'"></div>
            <p>{{item.trener2}}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import clubs from '@/components/clubs.js'
export default {
  data (){
    return{
      array: clubs
    }
  },
  mounted(){
    document.getElementById("4ok").style.display = "none";
  }
}
</script>

<style lang="css" scoped>
.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}
.block{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 20px;
  background-color: #222222;
  border-radius: 20px;
  padding: 20px;
  width: 80%;
  max-width: 600px;
  color: white;
}
.photo{
  width: 200px;
  height: 200px;
  background-size: cover;
  border-radius: 10px;
  margin-left: 20px;
}
.photo1{
  width: 200px;
  height: 200px;
  background-size: cover;
  border-radius: 10px;
}
.main{
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 80%;
}
.text{
  width: 80%;
  font-size: 15px;
  margin-top: 10px;
  margin-left: 20px;
}
h1{
  color: white;
}
@media (max-width: 650px) {
  .block{
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 20px;
    background-color: #222222;
    border-radius: 20px;
    padding: 20px 0px;
    width: 300px;
    color: white;
  }
  .text{
    width: 60%;
    font-size: 10px;
    margin-top: 10px;
  }
  h4{
    font-size: 12px;
  }
}
</style>
