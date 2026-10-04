from alembic import op
import sqlalchemy as sa
revision = "0001_users_profiles"
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("email", sa.String(320), nullable=False), sa.Column("hashed_password", sa.String(255), nullable=False), sa.Column("role", sa.Enum("STUDENT", "ADMIN", name="role"), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()))
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table("profiles", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), unique=True), sa.Column("full_name", sa.String(160), nullable=False, server_default=""), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()))
def downgrade():
    op.drop_table("profiles")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
