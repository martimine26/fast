<template lang="html">
  <section>
    <div class="container">
      <h1>Комитеты</h1>
      <div v-for="item in array" :key="item.id" class="main">
        <div class="block">
          <div class="photo" :style="{'background-image': 'url(' + require('@/assets/' + item.photo) + ')'}"></div>
          <div class="text">
            <h4>{{item.comi}}</h4>
            <p>{{item.text}}</p>
            <p>Члены комитета:</p>
            <p class="elem">{{item.name}}</p>
            <p class="elem">{{item.name1}}</p>
            <p class="elem">{{item.name2}}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import comiData from '@/components/comiData.js'
export default {
  data (){
    return{
      array: comiData
    }
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
  flex-direction: row;
  align-items: center;
  margin-top: 20px;
  background-color: #222222;
  border-radius: 20px;
  padding: 20px;
  width: 600px;
  color: white;
}
.photo{
  width: 200px;
  height: 200px;
  background-size: cover;
  border-radius: 10px;
}
.main{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.text{
  width: 60%;
  font-size: 15px;
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
.elem{
  margin-top: -20px;
}
</style>
