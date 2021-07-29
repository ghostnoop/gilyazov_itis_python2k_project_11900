<template>
  <div class="main__content--right">
    <div class="main__content--group" v-for="point in getPoints">
      <div class="content__group--title">
        <svg class="symbol__personal">
          <use xlink:href="#personal"></use>
        </svg>
        <span class="content__group--text">{{ point.name }}</span>
      </div>
      <div class="content__group--cards">


      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppMainContentLeft",
  computed: {
    getPoints() {
      return this.$store.getters['main/teams']
    }
  }
}
</script>

<style scoped>

</style>
