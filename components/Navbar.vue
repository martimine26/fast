<template lang="html">
  <section style="width:100%;">
    <div class="main">
      <div class="container" >
        <NuxtLink to="/"><img src="@/assets/logo-02-white.png" width="70px"></NuxtLink>
         <div class="mainNav">

           <NuxtLink to="/contacts" class="text-nav">Онлайн-музей реликвий оставшихся со второй мировой</NuxtLink>
         </div>
     </div>
    </div>
  </section>
</template>

<script>
export default {

  }
</script>

<style lang="css" scoped>
.main{
  display: flex;
  justify-content: center;
}
.container{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 100px;
  background-color: #222222;
  margin-top: 20px;
  width: 80%;
  border-radius: 20px;
  max-width: 1500px;
  padding: 30px;
}
.mainNav{
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 15px;
  z-index: 1;
}
.text-nav{
  position: relative;
  text-decoration: none;
  color: white;
  font-size: 16px;
  font-family: 'Rubik';
  margin-left: 20px;
  height: 40px;
}
.text-nav:after {
  content: "";
  position: absolute;
  width: 100%;
  height: 2px;
  left: 0;
  bottom: 10px;
  background: #cf8dcc;
  transition: transform .3s;
}
.text-nav:not(:hover):after {
  -webkit-transform: scalex(0);
  transform: scalex(0);
}
.block{
  margin-top: 50px;
  width: 500px;
  height: 500px;
  margin-left: 300px;
  background: linear-gradient(180deg, #7421B0 0%, #D08EFF 100%);
  border-top-left-radius: 70px;
  border-bottom-left-radius: 70px;
  display: flex;
  align-items:center;
  z-index: 2;
}
.hov{
  position: absolute;
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 200px;
  height: 200px;
  background-color: #910b96;
  border-radius: 20px;
  margin-top: 0px;
}
.service:hover .hov{
  display: flex;
  margin-top: 20px;
  z-index: 5;
}
.nav{
  width: 200px;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-left: 0px;
  padding-left: 10px;
}
.nav:hover{
  background-color: #ad3ba9;
  border-radius: 20px;
}
.nav:after{
  content: "";
  height: 0px;
}
img{
  padding: 10px;
}
.navigation{
  display: flex;
  flex-direction: column;
}
.user_logo{
  position: relative;
  text-decoration: none;
  color: white;
  font-size: 16px;
  width: 40px;
  margin-left: 20px;
}
@media (max-width: 1220px) {
  .text-nav{
    position: relative;
    text-decoration: none;
    color: white;
    font-size: 13px;
    font-family: 'Rubik';
    margin-left: 20px;
  }
  .nav{
    margin-left: 0px;
    padding-left: 10px;
  }
}
@media (max-width: 1000px) {
  .text-nav{
    position: relative;
    text-decoration: none;
    color: white;
    font-size: 13px;
    font-family: 'Rubik';
    margin-left: 10px;
  }
  .container{
    flex-direction: column;
    height: 200px;
    width: 100%;
  }
  .nav{
    margin-left: 0px;
    padding-left: 10px;
  }
  .text-nav:after {
    bottom: 18px;
  }
}
@media (max-width: 750px) {
  .text-nav{
    position: relative;
    text-decoration: none;
    color: white;
    font-size: 13px;
    font-family: 'Rubik';
    margin-left: 10px;
  }
  .nav{
    margin-left: 0px;
    padding-left: 10px;
  }
}
@media (max-width: 520px) {
  .text-nav{
    position: relative;
    text-decoration: none;
    color: white;
    font-size: 11px;
    font-family: 'Rubik';
    margin-left: 10px;
  }
  .nav{
    margin-left: 0px;
    padding-left: 10px;
  }
  .text-nav:after {
    bottom: 21px;
  }
}
@media (max-width: 450px) {
 .container{
   flex-direction: column;
   height: 340px;
   width: 100%;
 }
 .mainNav{
   flex-direction: column;
   margin-left: -10px;
 }
 .text-nav{
   font-size: 20px;
 }
 .nav{
   margin-left: 0px;
   padding-left: 10px;
 }
 .text-nav:after {
   bottom: 10px;
 }
}
</style>
