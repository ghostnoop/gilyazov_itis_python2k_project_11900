<template>
  <header class="main__header">
    <div class="main__header--right">

      <!--      <router-link to="/home" class="notext-decoration">-->
      <!--        <button class="main__header&#45;&#45;dashboard">-->
      <!--          <svg class="symbol__trello&#45;&#45;dashboard">-->
      <!--            <use xlink:href="#trello-dashboard"></use>-->
      <!--          </svg>-->
      <!--          <span class="header__dashboard-text">Дqски</span>-->
      <!--        </button>-->

      <!--      </router-link>-->
    </div>
    <div class="main__header--middle">

      <router-link to="/orders" class="notext-decoration">
        <button class="main__header--dashboard">Заказы</button>
      </router-link>

      <router-link to="/points" class="notext-decoration">
        <button class="main__header--dashboard">Точки</button>
      </router-link>

      <router-link to="/executors" class="notext-decoration">
        <button class="main__header--dashboard">Исполнители</button>
      </router-link>

      <router-link to="/main" class="notext-decoration">
        <button class="main__header--dashboard">Главная</button>
      </router-link>

      <router-link to="/services" class="notext-decoration">
        <button class="main__header--dashboard">Сервисы</button>
      </router-link>


      <router-link to="/disputes" class="notext-decoration">
        <button class="main__header--dashboard">Споры</button>
      </router-link>

      <router-link to="/map" class="notext-decoration">
        <button class="main__header--dashboard">Карта</button>
      </router-link>

      <router-link to="/logout" class="notext-decoration">
        <button class="main__header--dashboard">Выход</button>
      </router-link>


    </div>
    <div class="main__header--left">

    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeaderMain",
  data: () => ({}),
  methods: {
    clickMenu() {
      this.$store.commit('clickMenu')
    },
    clickCreateBoard() {
      this.$store.commit('activeModalBoard')
    }
  },
}
</script>

<style scoped>

</style>
