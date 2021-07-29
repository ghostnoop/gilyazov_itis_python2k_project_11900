<template>
    <div class="header__board--popup" v-bind:class="{'popup__active':activePopup}">
        <div class="header__board--title">
          <button class="board__avatar--popup">
            ДГ
          </button>
          <div class="header__popup--info">
            <span class="header__popup--username">Дмитрий Герасимов</span>
            <span class="header__popup--email">dmitry.iti.ger@gmail.com</span>
          </div>

          <svg class="symbol__close--popup" v-on:click="closePopup">
            <use xlink:href="#close"></use>
          </svg>
        </div>
      <div class="header__popup--content">
        <a href="#" class="header__popup--a">Удалить с доски...</a>
      </div>
    </div>
</template>

<script>
export default {
  name: "AppPopupMember",
  computed: {
    activePopup(){
      return this.$store.state.activePopup
    },
    closePopup(){
      return this.$store.commit('activePopup')
    }
  }
}
</script>

<style scoped>

</style>