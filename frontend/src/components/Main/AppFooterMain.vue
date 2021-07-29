<template>
  <footer class="footer">
      <div class="container">
        <span class="text-muted">Это Footer. Сделанный в VueJs</span>
      </div>
    </footer>
</template>

<script>
export default {
  name: "AppFooterMain",
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
