<template>
  <div class="container">
    <Navbar />
    <Nuxt />
  </div>
</template>

<script type="text/javascript">
import Navbar from '@/components/Navbar.vue'
  export default{
    components:{
      Navbar
    }
  }
</script>

<style scoped>
.container{
  background-color: #111111; 
}
</style>
