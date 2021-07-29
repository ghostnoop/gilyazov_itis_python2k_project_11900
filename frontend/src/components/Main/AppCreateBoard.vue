<template>
  <div class="create_team--window" v-bind:class="{'team__window--active':activeModal}">
    <div class="create_team--modal">
      <svg class="symbol__close--modal" v-on:click="closeModal">
        <use xlink:href="#close"></use>
      </svg>
      <div class="team__modal--info">
        <form class="team__modal--form">
          <span class="team__modal--title">Создайте доску</span>
          <span class="team__modal--text">Повысьте удобство: создайте доску для комфортной работы.</span>
          <div class="modal__group">
            <label for="name_board" class="modal__team--label">Название доски</label>
            <input type="text" id="name_board" class="modal__team--input" placeholder="Введите название доски">
            <div class="modal__team-undertext">Укажите название доски.</div>
          </div>

          <div class="modal__group">
            <label for="name_team" class="modal__team--label">Выберите команду</label>
            <select name="name_team" class="modal__team--input" id="name_team">
              <option value="Выберите команду">Выберите команду</option>
              <option value="Best coders">Best coders</option>
            </select>
          </div>

          <button class="modal__team--btn">Создать доску</button>
        </form>
      </div>
      <div class="modal__team--background">
        <div class="modal__team--photo">
          <img src="img/empty-board.d1f066971350650d3346.svg" class="modal__team--img" alt="">
          <img src="img/green-face.1a4590e4c12ebbbd161a.svg" alt="" class="modal__team--subimg">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppCreateBoard",
  computed: {
    activeModal() {
      return this.$store.state.activeBoardModal;
    }
  },
  methods: {
    closeModal() {
      this.$store.commit('activeModalBoard')
    }
  }
}
</script>

<style scoped>

</style>