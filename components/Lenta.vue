<template lang="html">
  <section>
    <div class="main">
      <div class="block">
        <h3>Здравствуйте,на нашем сайте вы можете увидеть реликвии семей участников Великой Отечественной войны,которые передаются из поколения в поколение</h3>
      </div>
    </div>
  </section>
</template>

<script>
import posts from '@/components/posts.js'
export default {
  data (){
    return{
      array: posts
    }
  },
  methods:{

  }
}
</script>

<style lang="css" scoped>
h3{
  color: white
}
.main{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.block{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  background-color: #222222;
  border-radius: 20px;
  width: 80%;
  padding: 30px;
}
p{
  color: white;
  width: 40%;
  margin-top: 20px;
}
.new{
  width: 100%;
  height: 300px;
  background-size: cover;
  border-radius: 20px;
  display: flex;
  flex-direction: row;
  margin-top: -25px;
}
.text{
  display: flex;
  flex-direction: row;
  align-items: center;
  color: white;
}
button{
  background: none;
  border: none;
}
.one{
  flex-direction: row;
}
.two{
  flex-direction: row-reverse;
}
img{
  color: white;
  width: 35px;
}
@media (max-width: 450px) {
.block{
  flex-direction: column;
  width: 100%;
  height: 800px;
  font-size: 10px;
  padding: 5px;
  padding-top: 10px;
}
.new{
  flex-direction: column;
}
img{
  width: 20px;
}
}
@media (max-width: 995px) {
.block{
  flex-direction: column;
  width: 100%;
  height: 800px;
  font-size: 10px;
}
.new{
  flex-direction: column;
}
.text{
  align-items: flex-start;
  min-width: 250px;
}
}
@media (max-width: 366px) {

 .block{
   width: 100%;
 }
 img{
   width: 35px;
   position: absolute;
 }
 #swi1{
   margin-left: -40px;
 }
}
</style>
