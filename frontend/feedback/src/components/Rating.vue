<template>
  <div>
    <h1>How would you rate your satisfaction with our product?</h1>
    <star-rating 
      v-model="rating" 
      v-bind:increment="1"
      v-bind:max-rating="5"
      inactive-color="#B6B3B3"
      active-color="#474545"
      v-bind:star-size="90"
      @rating-selected ="setRating"
      >
    </star-rating>
    <div>Very disatisfied <span style="margin-left:200px;">Very satisfied</span></div>
    
  </div>
</template>

<script type="text/javascript">   
import StarRating from 'vue-star-rating';

export default{
  components: {
    StarRating
  },
  data(){
    return {
      rating: 3
    }
  },
  methods: {
    setRating: function(rating){
      this.rating= rating;
      
      const requestOptions = {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: "kubilk56@gmail.com",rating:this.rating })
      };

      //request to api

      fetch("http://127.0.0.1:8000/feedback/update", requestOptions)
      .then(response => response.json())
      .then(data => (this.postId = data.id));
      }
  },
}
</script>