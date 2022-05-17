<template lang="html">
  <section style="width:100%">
    <div class="main">
      <div class="photo" :style="{'background-image': 'url(' + require('@/assets/' + array[array.length - 1 - $route.params.id].photo) + ')'}"></div>
      <p>{{ array[array.length - 1 - $route.params.id].text}}</p>
    </div>
  </section>
</template>

<script>
import slide from '@/components/slide.js'
export default {
  data(){
    return{
      array: slide
    }
  }
}
</script>

<style lang="css" scoped>

section{
  display: flex;
  justify-content: center;
}
.main{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  background-color: #222222;
  border-radius: 20px;
  width: 100%;
  padding: 30px;
}
.photo{
  width: 80%;
  max-width: 600px;
  min-height: 300px;
  height: 80%;
  max-height: 500px;
  background-size: cover;
  border-radius: 20px;
}
p{
  color: white;
  width: 80%;
  margin-top: 20px;
  max-width: 600px;
}
@media (min-width: 1000px) {
 .main{
   width: 80%;
 }
}
@media (max-width: 450px) {
  .photo{
    width: 100%;
  }
  p{
    width: 100%;
    font-size: 15px;
  }
}
</style>
