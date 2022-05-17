<template lang="html">
  <div class="main">
    <div class="slider">
      <button type="button" @click="Switch0()" id="buttonLeft" style="z-index:1">

      </button>
      <div v-for="item in stas"
      :key="item.id"
      :style="{'display': item.display , 'z-index': 0,}"
      :id="item.id + 'lmao'"
      class="slide"
      >
      <div class="divText">
        <p class="text">{{item.text}}</p>
      </div>
      </div>
      <button type="button" @click="SwitchTwo0()" id="buttonRight" style="z-index:1" ref="bR">

      </button>
    </div>
  </div>
</template>

<script>
import slide from '@/components/slide.js'
export default {
  data(){
    return{
      counta:0,
      stas: slide
    }
  },
  mounted(){

  },
  methods:{
    Switch0(){
    let self = this;
    let elemOne = document.getElementById(`${this.counta - 1}lmao`);
    let elemTwo = document.getElementById(`${this.counta}lmao`);
    if(this.counta > 0){
      elemOne.style.marginLeft = "0px"
      this.counta -= 1
     }
     else{
       this.counta = this.stas.length - 1;
       for (let i = 0; i < this.counta; i++) {
         let element = document.getElementById(`${i}lmao`)
         function delay(elem){
           elem.style.marginLeft = '500px';
           function del(){
             elem.style.display = 'block';
           }
           setTimeout(del,500)
         }
         setTimeout(delay(element), 50)
       }
     }
    },
    SwitchTwo0(){
    let self = this;
    let elemOne = document.getElementById(`${this.counta - 1}lmao`);
    let elemTwo = document.getElementById(`${this.counta}lmao`);
      if(this.counta < this.stas.length - 1){
          function animation(elem){
            elem.style.marginLeft = '-500px';
            if(self.counta < self.stas.length ){
              setTimeout(function delay(){
                elem.style.display = 'none';
                elem.style.marginLeft = '500px';
                  setTimeout(function del(){
                    elem.style.display = 'block';
                  },50)
              },500)
            }
          }
        animation(elemTwo)
        this.counta += 1;
      }
      else{
      for (let i = 1; i < this.stas.length; i++) {
          let elems0 = document.getElementById(`${i - 1}lmao`);
          elems0.style.marginLeft = "0px";
        }
        this.counta = 0;
      }
    }
  }
}
</script>

<style lang="css" scoped>
.main{
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  width: 100%;
  margin-left: 20px;
}
.slider{
  position: relative;
  width: 100%;
	height: 100%;
	margin: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
  min-height: 250px;
  min-width: 350px;
  max-width: 400px;
}
.slide{
  width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
  transition: 0.55s;
  background-color: #222222;

}
.sli1{
  background: green;
}
.sli2{
  background: red;
}
.sli3{
  background: blue;
}
button{
  background: none;
  border: none;
  width: 50px;
  height: 50px;
}
svg{
  color: white;
}
.divText{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
@media (max-width: 995px) {
 .slider{
   min-width: 150px;
 }
}
@media (max-width: 450px) {
  .text{
    font-size: 15px;
  }
  .slider{
    margin-top: 25px;
  }
}
@media (max-width: 366px) {
  .main{
    margin-left: -30px;
    overflow-x: none;
  }
  .slider{
    margin-left: 20px;
  }
}
</style>
