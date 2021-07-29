<template>
  <div class="main__content--group" v-for="point in getPoints">
    <div class="card__list--cards">

      <span class="content__group--text">{{ point.surname }} {{ point.name }} {{ point.last_name }}</span>
      <br>
      <span class="content__group--text">{{ point.birth_date }} {{ point.dead_date }} </span>
    </div>
    <br>


  </div>
</template>

<script>
import store from "@/store";

export default {
  name: "AppPointCard",
  computed: {
    getPoints() {
      return this.$store.getters['main/teams']
    }
  }
}
</script>

<style scoped>

</style>
