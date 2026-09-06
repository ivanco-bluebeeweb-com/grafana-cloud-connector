# Grafana Cloud Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Grafana Service Account Token (Authorization: Bearer <token>)
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /api/org`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
