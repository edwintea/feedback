<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="greetings">
    
    <h3>
      <!--RENDER STAR HERE-->
    </h3>
  </div>
</template>

<style scoped>

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: left;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    display: block;
    text-align: left;
  }
}
</style>
