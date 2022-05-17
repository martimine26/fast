<template lang="html">
  <section>
    <div class="main">
      <div class="photo" :style="{'background-image': 'url(' + require('@/assets/rel/' + array[$route.params.id].photo) + ')'}"></div>
      <div class="two">
        <h2>{{array[$route.params.id].zag}}</h2>
        <p>{{array[$route.params.id].text}}</p>
      </div>
    </div>
  </section>
</template>

<script>
import clubs from '@/components/clubs.js'
export default {
  data(){
    return{
      array: clubs
     }
    },
  }
</script>

<style lang="css" scoped>
 .photo{
   width: 1200px;
   height: 350px;
   background-size: cover;
 }
  section{
    display: flex;
    justify-content: center;
  }
  #one{
    display: none;
  }
  .main{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-content: center;
    width: 80%;
    max-width: 600px;
    margin-top: 20px;
  }
  .two{
    display: flex;
    flex-direction: column;
  }
  h2{
    color: white;
    margin-left: 10px;
  }
  p{
    color: white;
    margin-left: 10px;
    margin-top: 20px;
  }
</style>
