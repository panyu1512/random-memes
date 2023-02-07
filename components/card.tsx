import styles from '@/styles/Card.module.css'
export default function Card({title, src_img}: {title: string, src_img: string}){
    return (
        <div className={styles.card}>
            <img className={styles.img} src={src_img} alt={title} />
            <h3>{title}</h3>
        </div>
    )
}