import styles from '@/styles/Card.module.css'
export default function Card({title, src_img, alt}: {title: string, src_img: string, alt: string}){
    return (
        <div className={styles.card}>
            <img src={src_img} alt={alt} />
            <h3>{title}</h3>
        </div>
    )
}