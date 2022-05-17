<template lang="html">
  <div class="main">
    <div class="slider">
      <button type="button" @click="Switch()" id="buttonLef" style="z-index:1">

      </button>
      <div v-for="item in stas"
      :key="item.id"
      :style="{'background-image': 'url(' + require('@/assets/' + item.photo) + ')', 'display': item.display , 'z-index': 0,}"
      :id="item.id"
      class="slide"
       @click.prevent="openNews(item)"
      >

      </div>
      <button type="button" @click="SwitchTwo()" id="buttonRigh" style="z-index:1" ref="bR">

      </button>
    </div>
  </div>
</template>

<script>
import slide from '@/components/slide.js'
export default {
  data(){
    return{
      count:0,
      stas: slide
    }
  },
  mounted(){

  },
  methods:{
    Switch(){
    let self = this;
    let elemOne = document.getElementById(this.count - 1);
    let elemTwo = document.getElementById(this.count);
    if(this.count > 0){
      elemOne.style.marginLeft = "0px"
      this.count -= 1
     }
     else{
       this.count = this.stas.length - 1;
       for (let i = 0; i < this.count; i++) {
         let element = document.getElementById(i)
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
    SwitchTwo(){
    let self = this;
    let elemOne = document.getElementById(this.count - 1);
    let elemTwo = document.getElementById(this.count);
      if(this.count < this.stas.length - 1){
          function animation(elem){
            elem.style.marginLeft = '-500px';
            if(self.count < self.stas.length ){
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
        this.count += 1;
      }
      else{
      for (let i = 1; i < this.stas.length; i++) {
          let elems = document.getElementById(i - 1);
          elems.style.marginLeft = "0px";
        }
        this.count = 0;
      }
    },
    openNews(item) {
      this.$router.push('/news/' + item.id)
    },
  }
}
</script>

<style lang="css" scoped>
.main{
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  width: 100%;
  cursor: pointer;
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
  border-radius: 20px;
  min-height: 200px;
  max-width: 400px;
}
.slide{
  width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
  transition: 0.55s;
  background-size: cover;
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
.text{
  color: white;
}
</style>
