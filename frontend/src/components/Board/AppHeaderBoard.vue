<template>
  <header class="header__board">
    <div class="header__board--right">
      <div class="header__board-item">
        Best_coder mainer
      </div>
      <div class="vertical__line"></div>
      <div class="header__board-team">Best coders</div>
      <div class="vertical__line"></div>
      <div class="header__board--members">
        <div class="header__board--member-block admin">
          <button class="main__header--username board__avatar" v-on:click="openPopup">
            ДГ
          </button>
          <span class="admin__symbol"></span>
        </div>
        <button class="main__header--username board__avatar ">
          RM
        </button>
      </div>

      <div class="vertical__line"></div>
      <div class="header__board-team" v-on:click="clickInvitation">Пригласить</div>
    </div>
    <div class="header__board--left">
      <button class="header__board-team header__board--menu" v-on:click="clickArchive">Архив</button>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeaderBoard",
  methods: {
    clickInvitation() {
      this.$store.commit('activateInvitation')
    },
    clickArchive() {
      this.$store.commit('activateArchive')
    },
    openPopup() {
      this.$store.commit('activePopup')
    },
  }
}
</script>

<style scoped>

</style>