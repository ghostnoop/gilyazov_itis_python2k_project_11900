<template>
  <div class="card-container" v-on:click="clickCard">
    <div class="card-body">
      <p>
        {{ text }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppCard",
  props: {
    id: Number,
    text: String,
  },
  methods: {
    clickCard() {
      this.$store.commit('activateCard')
    }
  }
}
</script>

<style scoped>

</style>