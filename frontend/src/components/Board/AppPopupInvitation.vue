<template>
  <div class="popup__section--invitation" v-bind:class="{'active__invitation':activeInvitation}">
    <div class="popup__invitation">
      <svg class="symbol__close--invitation" v-on:click="closeInvitation">
        <use xlink:href="#close"></use>
      </svg>
      <div class="popup__invitation--title">
        Пригласить на доску
      </div>
      <form class="popup__invitation--form">
        <div class="popup__invitation--group">
          <input type="text" placeholder="Адрес электронной почты" class="popup__invitation--input">
          <div class="popup__invitation--searched">
            <a href="#" class="popup__invitation--item notext-decoration">
              <div class="main__header--username board__avatar">
                ДГ
              </div>
              <div class="popup__invitation--email">dmitryitit@gmail.com</div>
            </a>

          </div>
        </div>
        <button class="popup__invitation--btn">Отправить приглашение</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppPopupInvitation",
  computed: {
    activeInvitation() {
      return this.$store.state.activeInvitation;
    },
    closeInvitation() {
      this.$store.commit('activateInvitation')
    }
  }
}
</script>

<style scoped>

</style>