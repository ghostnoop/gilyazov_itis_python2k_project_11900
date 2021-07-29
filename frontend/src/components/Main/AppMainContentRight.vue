<template>
  <div class="main__content--left">

    <div class="main__content--block">
      <div class="main__content--title">
        <span class="main__content--titleText">Точки</span>

      </div>
      <button class="main__content--item" v-for="team in getTeams">
        <svg class="symbol__group--content">
          <use xlink:href="#group"></use>
        </svg>
        <span class="main__content--text">{{ team.name }}</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppMainContentRight",
  data: () => ({
    teams: []
  }),
  computed: {
    getTeams() {
      return this.$store.getters['main/teams']
    }
  },
  methods: {
    clickPlus() {
      this.$store.commit('activeModal');
    }
  },
  mounted() {
    this.$store.dispatch('main/mountTeams')
  }
}
</script>

<style scoped>

</style>
