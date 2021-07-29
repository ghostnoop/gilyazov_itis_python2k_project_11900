<template>
  <div class="menu__board" v-bind:class="{'active__menu':activeArchive}">
    <div class="menu__board--title">
      Архив
      <svg class="symbol__close--menu" v-on:click="closeArchive">
        <use xlink:href="#close"></use>
      </svg>
    </div>
    <div class="menu__board--content">
      <div class="menu__board--item">
        <a href="#" class="menu__board--card notext-decoration">
          <span class="archive__name">создание регистрации</span>
        </a>
        <p class="menu__board--action">
          <a href="#" class="link__back">Вернуть на доску</a>
          <span class="notext-decoration delitel"> - </span>
          <a href="#" class="link__delete">Удалить</a>
        </p>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "AppBoardMenu",
  computed: {
    activeArchive() {
      return this.$store.state.activeArchive
    }
  },
  methods: {
    closeArchive() {
      this.$store.commit('activateArchive')
    }
  }
}
</script>

<style scoped>

</style>